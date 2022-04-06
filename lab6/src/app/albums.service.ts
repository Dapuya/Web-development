import { Injectable } from '@angular/core';
import {ALBUMS} from "./fake-db";
import {Observable} from "rxjs";
import {Album, Photos} from "./models";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})

export class AlbumsService {

  BASE_URL= 'https://jsonplaceholder.typicode.com'

  constructor(private client: HttpClient) {}

  getAlbums(): Observable<Album[]> {
    return this.client.get<Album[]>(`${this.BASE_URL}/albums`);
  }

  getAlbum(id: number): Observable<Album> {
    return this.client.get<Album>(`${this.BASE_URL}/albums/${id}`);
  }

  addAlbum(album: Album): Observable<Album> {
    return this.client.post<Album>(`${this.BASE_URL}/albums`, album);
  }

  updateAlbum(album: Album): Observable<Album> {
    return this.client.put<Album>(`${this.BASE_URL}/albums/${album.id}`, album);
  }

  deleteAlbum(id: number): Observable<any> {
    return this.client.delete(`${this.BASE_URL}/albums/${id}`);
  }

  getAlbumPhotos(id: number): Observable<Photos[]> {
    return this.client.get<Photos[]>(`${this.BASE_URL}/albums/${id}/photos`);
  }

}
